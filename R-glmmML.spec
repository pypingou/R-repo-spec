%global packname  glmmML
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.82.1
Release:          1%{?dist}
Summary:          Generalized linear models with clustering

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.82-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Binary and Poisson regression for clustered data, fixed and random effects
with bootstrapping.

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
%doc %{rlibdir}/glmmML/html
%doc %{rlibdir}/glmmML/DESCRIPTION
%doc %{rlibdir}/glmmML/doc
%{rlibdir}/glmmML/Meta
%{rlibdir}/glmmML/NAMESPACE
%{rlibdir}/glmmML/libs
%{rlibdir}/glmmML/R
%{rlibdir}/glmmML/help
%{rlibdir}/glmmML/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.82.1-1
- initial package for Fedora