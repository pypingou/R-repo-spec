%global packname  longpower
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Sample size calculations for longitudinal data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Matrix R-lme4 R-methods 


BuildRequires:    R-devel tex(latex) R-Matrix R-lme4 R-methods



%description
The longpower package contains functions for computing power and sample
size for linear models of longitudinal data based on the formula due to
Liu and Liang (1997) and Diggle et al (2002). Either formula is expressed
in terms of marginal model or Generalized Estimating Equations (GEE)
parameters. This package contains functions which translate pilot mixed
effect model parameters (e.g. random intercept and/or slope) into marginal
model parameters so that the formulas of Diggle et al or Liu and Liang
formula can be applied to produce sample size calculations for two sample
longitudinal designs assuming known variance.

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
%doc %{rlibdir}/longpower/html
%doc %{rlibdir}/longpower/DESCRIPTION
%doc %{rlibdir}/longpower/CITATION
%doc %{rlibdir}/longpower/doc
%{rlibdir}/longpower/help
%{rlibdir}/longpower/NAMESPACE
%{rlibdir}/longpower/R
%{rlibdir}/longpower/INDEX
%{rlibdir}/longpower/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora