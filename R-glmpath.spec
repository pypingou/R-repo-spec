%global packname  glmpath
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.95
Release:          1%{?dist}
Summary:          L1 Regularization Path for Generalized Linear Models and Cox Proportional Hazards Model

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
A path-following algorithm for L1 regularized generalized linear models
and Cox proportional hazards model

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
%doc %{rlibdir}/glmpath/html
%doc %{rlibdir}/glmpath/DESCRIPTION
%{rlibdir}/glmpath/INDEX
%{rlibdir}/glmpath/NAMESPACE
%{rlibdir}/glmpath/help
%{rlibdir}/glmpath/data
%{rlibdir}/glmpath/R
RPM build errors:
%{rlibdir}/glmpath/Meta
%{rlibdir}/glmpath/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.95-1
- initial package for Fedora