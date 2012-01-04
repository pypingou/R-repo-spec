%global packname  metafor
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Meta-Analysis Package for R

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.6-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-nlme R-Formula 

BuildRequires:    R-devel tex(latex) R-stats R-nlme R-Formula 

%description
The metafor package consists of a collection of functions for conducting
meta-analyses in R. The package includes functions to calculate various
effect size or outcome measures, fit fixed-, random-, and mixed-effects
models to such data, carry out moderator and meta-regression analyses, and
create various types of meta-analytical plots (e.g., forest, funnel,
radial, and L'Abbe plots). For meta-analyses of 2x2 table data, the
Mantel-Haenszel and Peto's method are also implemented.

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
%doc %{rlibdir}/metafor/html
%doc %{rlibdir}/metafor/DESCRIPTION
%doc %{rlibdir}/metafor/NEWS
%doc %{rlibdir}/metafor/CITATION
%doc %{rlibdir}/metafor/doc
%{rlibdir}/metafor/NAMESPACE
%{rlibdir}/metafor/Meta
%{rlibdir}/metafor/INDEX
%{rlibdir}/metafor/R
%{rlibdir}/metafor/help
%{rlibdir}/metafor/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora