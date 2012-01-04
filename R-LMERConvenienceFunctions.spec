%global packname  LMERConvenienceFunctions
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.6.6
Release:          1%{?dist}
Summary:          A suite of functions to back-fit fixed effects and forward-fit random effects, as well as other miscellaneous functions.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-languageR R-Matrix R-lme4 


BuildRequires:    R-devel tex(latex) R-languageR R-Matrix R-lme4



%description
Functions to back-fit fixed effects (on F or t values and, potentially,
log-likelihood ratio testing) and to forward-fit random effects (using
log-likelihood ratio testing). Note that the back- and forward-fitting of
generalized linear mixed-effects regression (\code{glmer}s) models is not
yet supported. The package also includes a function to compute ANOVAs with
upper- and lower-bound p-values (anti-conservative and conservative,
respectively), a function to graph model criticism plots, functions to
trim data on model residuals or on a response variable (per subject), a
function to perform posthoc analyses, a function to generate (dynamic) 3d
plots of (i) predicted values of an LMER model for interactions between
two numeric variables,(ii) the raw data as a function of two numeric
variable, and (iii) kernel density estimates (densities) of two numeric

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
%doc %{rlibdir}/LMERConvenienceFunctions/NEWS
%doc %{rlibdir}/LMERConvenienceFunctions/DESCRIPTION
%doc %{rlibdir}/LMERConvenienceFunctions/html
%{rlibdir}/LMERConvenienceFunctions/data
%{rlibdir}/LMERConvenienceFunctions/help
%{rlibdir}/LMERConvenienceFunctions/INDEX
%{rlibdir}/LMERConvenienceFunctions/NAMESPACE
%{rlibdir}/LMERConvenienceFunctions/Meta
%{rlibdir}/LMERConvenienceFunctions/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.6-1
- initial package for Fedora