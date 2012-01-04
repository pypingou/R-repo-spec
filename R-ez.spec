%global packname  ez
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.0.0
Release:          1%{?dist}
Summary:          Easy analysis and visualization of factorial experiments.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_3.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-car R-reshape2 R-plyr R-ggplot2 R-stringr R-lme4 R-Matrix 

BuildRequires:    R-devel tex(latex) R-car R-reshape2 R-plyr R-ggplot2 R-stringr R-lme4 R-Matrix 

%description
This package facilitates easy analysis of factorial experiments, including
purely within-Ss designs (a.k.a. "repeated measures"), purely between-Ss
designs, and mixed within-and-between-Ss designs. The functions in this
package aim to provide simple, intuitive and consistent specification of
data analysis and visualization. Visualization functions also include
design visualization for pre-analysis data auditing, and correlation
matrix visualization. Finally, this package includes functions for
non-parametric analysis, including permutation tests and bootstrap
resampling. The bootstrap function obtains predictions either by cell
means or by more advanced/powerful mixed effects models, yielding
predictions and confidence intervals that may be easily visualized at any
level of the experiment's design.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.0.0-1
- initial package for Fedora