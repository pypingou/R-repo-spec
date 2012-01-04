%global packname  mondate
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.8.24
Release:          1%{?dist}
Summary:          Keep track of dates in terms of months

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-utils R-methods 

BuildRequires:    R-devel tex(latex) R-utils R-methods 

%description
Keep track of dates in month units. Perform date arithmetic in "months"
(default), "years", and "days". Enable dates to have "shape" (non NULL
dim). Allow "infinite" dates.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/mondate/DESCRIPTION
%doc %{rlibdir}/mondate/html
%{rlibdir}/mondate/Meta
%{rlibdir}/mondate/INDEX
%{rlibdir}/mondate/R
%{rlibdir}/mondate/NAMESPACE
%{rlibdir}/mondate/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.8.24-1
- initial package for Fedora