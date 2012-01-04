%global packname  gwrr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Geographically weighted regression with penalties and diagnostic tools

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-fields 


BuildRequires:    R-devel tex(latex) R-fields



%description
Fits geographically weighted regression (GWR) models and uses tools to
diagnose collinearity in the GWR models.

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
%doc %{rlibdir}/gwrr/html
%doc %{rlibdir}/gwrr/DESCRIPTION
%{rlibdir}/gwrr/Meta
%{rlibdir}/gwrr/data
%{rlibdir}/gwrr/R
%{rlibdir}/gwrr/NAMESPACE
%{rlibdir}/gwrr/help
%{rlibdir}/gwrr/INDEX

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora