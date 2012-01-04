%global packname  CNVassoc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Association analysis of CNV data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mixdist R-mclust R-survival 

BuildRequires:    R-devel tex(latex) R-mixdist R-mclust R-survival 

%description
This package carries out association analysis of common copy number
variants in population-based studies. This package includes functions for
analysing association under a series of study designs (case-control,
cohort, etc), using several dependent variables (class status, censored
data, counts) as response, adjusting for covariates and considering
various inheritance models. It also includes functions for inferring copy
number (CNV genotype calling).  Various classes and generic functions
(print, summary, plot, anova, ... ) have been created to facilitate the

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
%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora