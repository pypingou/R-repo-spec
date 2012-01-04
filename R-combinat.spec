%global packname  combinat
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.8
Release:          1%{?dist}
Summary:          combinatorics utilities

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
routines for combinatorics

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
%doc %{rlibdir}/combinat/html
%doc %{rlibdir}/combinat/DESCRIPTION
%{rlibdir}/combinat/INDEX
%{rlibdir}/combinat/Meta
%{rlibdir}/combinat/R
%{rlibdir}/combinat/NAMESPACE
%{rlibdir}/combinat/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.8-1
- initial package for Fedora