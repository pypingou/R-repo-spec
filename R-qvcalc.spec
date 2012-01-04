%global packname  qvcalc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8.7
Release:          1%{?dist}
Summary:          Quasi variances for factor effects in statistical models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Functions to compute quasi variances and associated measures of
approximation error

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
%doc %{rlibdir}/qvcalc/DESCRIPTION
%doc %{rlibdir}/qvcalc/html
%{rlibdir}/qvcalc/INDEX
%{rlibdir}/qvcalc/NAMESPACE
%{rlibdir}/qvcalc/R
%{rlibdir}/qvcalc/Meta
%{rlibdir}/qvcalc/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.7-1
- initial package for Fedora