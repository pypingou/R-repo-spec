%global packname  ROCR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Visualizing the performance of scoring classifiers.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-gplots R-methods 


BuildRequires:    R-devel tex(latex) R-gplots R-methods



%description
ROC graphs, sensitivity/specificity curves, lift charts, and
precision/recall plots are popular examples of trade-off visualizations
for specific pairs of performance measures. ROCR is a flexible tool for
creating cutoff-parametrized 2D performance curves by freely combining two
from over 25 performance measures (new performance measures can be added
using a standard interface). Curves from different cross-validation or
bootstrapping runs can be averaged by different methods, and standard
deviations, standard errors or box plots can be used to visualize the
variability across the runs. The parametrization can be visualized by
printing cutoff values at the corresponding curve positions, or by
coloring the curve according to cutoff. All components of a performance
plot can be quickly adjusted using a flexible parameter dispatching
mechanism. Despite its flexibility, ROCR is easy to use, with only three
commands and reasonable default values for all optional parameters.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.4-1
- initial package for Fedora