%global packname  blme
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.01.4
Release:          1%{?dist}
Summary:          Bayesian Linear Mixed-Effects models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.01-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Matrix R-lme4 
Requires:         R-lme4 R-Matrix 

BuildRequires:    R-devel tex(latex) R-methods R-Matrix R-lme4
BuildRequires:    R-lme4 R-Matrix 


%description
Maximum a posteriori estimation for linear and generalized linear
mixed-effects models in a Bayesian setting. Extends lme4 by Douglas Bates
and Martin Maechler.

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
%doc %{rlibdir}/blme/html
%doc %{rlibdir}/blme/DESCRIPTION
%doc %{rlibdir}/blme/doc
%{rlibdir}/blme/Meta
%{rlibdir}/blme/NAMESPACE
%{rlibdir}/blme/libs
%{rlibdir}/blme/R
%{rlibdir}/blme/help
%{rlibdir}/blme/INDEX
%{rlibdir}/blme/unitTests

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.01.4-1
- initial package for Fedora