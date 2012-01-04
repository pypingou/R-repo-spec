%global packname  EMA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Easy Microarray data Analysis

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-cluster R-heatmap.plus R-FactoMineR R-GOstats R-survival R-multtest R-gcrma R-rgl R-GSA R-RankProd R-siggenes R-MASS R-biomaRt R-xtable R-AnnotationDbi 

BuildRequires:    R-devel tex(latex) R-cluster R-heatmap.plus R-FactoMineR R-GOstats R-survival R-multtest R-gcrma R-rgl R-GSA R-RankProd R-siggenes R-MASS R-biomaRt R-xtable R-AnnotationDbi 

%description
Based on the experience of biostatisticians of Institut Curie, we propose
both a clear analysis strategy and a selection of tools to investigate
microarray gene expression data. The most usual and relevant existing R
functions were discussed, validated and gathered in an easy-to-use R
package (EMA) devoted to gene expression microarray analysis. These
functions were improved for ease of use, enhanced visualisation and better
interpretation of results.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.1-1
- initial package for Fedora