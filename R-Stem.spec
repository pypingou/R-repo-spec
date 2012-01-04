%global packname  Stem
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Spatio-temporal models in R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm R-MASS 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-MASS 

%description
Estimation of the parameters of a spatio-temporal model using the EM
algorithm, estimation of the parameter standard errors using a
spatio-temporal parametric bootstrap, spatial mapping.

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
%doc %{rlibdir}/Stem/html
%doc %{rlibdir}/Stem/DESCRIPTION
%{rlibdir}/Stem/R
%{rlibdir}/Stem/data
%{rlibdir}/Stem/help
%{rlibdir}/Stem/INDEX
%{rlibdir}/Stem/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora