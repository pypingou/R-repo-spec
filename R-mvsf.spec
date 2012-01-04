%global packname  mvsf
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Shapiro-Francia Multivariate Normality Test

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-nortest R-mvnormtest 

BuildRequires:    R-devel tex(latex) R-nortest R-mvnormtest 

%description
Generalization of the Shapiro-Francia test for multivariate variables.

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
%doc %{rlibdir}/mvsf/html
%doc %{rlibdir}/mvsf/DESCRIPTION
%doc %{rlibdir}/mvsf/COPYING
%{rlibdir}/mvsf/help
%{rlibdir}/mvsf/Meta
%{rlibdir}/mvsf/R
%{rlibdir}/mvsf/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora