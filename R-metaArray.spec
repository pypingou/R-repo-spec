%global packname  metaArray
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.32.0
Release:          1%{?dist}
Summary:          Integration of Microarray Data for Meta-analysis

Group:            Applications/Engineering 
License:          LGPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-Biobase R-MergeMaid R-graphics R-stats 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-Biobase R-MergeMaid R-graphics R-stats 


%description
1) Data transformation for meta-analysis of microarray Data:
Transformation of gene expression data to signed probability scale
(MCMC/EM methods) 2) Combined differential expression on raw scale:
Weighted Z-score after stabilizing mean-variance relation within platform

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
%doc %{rlibdir}/metaArray/doc
%doc %{rlibdir}/metaArray/html
%doc %{rlibdir}/metaArray/DESCRIPTION
%{rlibdir}/metaArray/data
%{rlibdir}/metaArray/INDEX
%{rlibdir}/metaArray/libs
%{rlibdir}/metaArray/Meta
%{rlibdir}/metaArray/NAMESPACE
%{rlibdir}/metaArray/R
%{rlibdir}/metaArray/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.32.0-1
- initial package for Fedora