%global packname  safe
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.14.0
Release:          1%{?dist}
Summary:          Significance Analysis of Function and Expression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-annotate R-methods 
Requires:         R-SparseM R-GO.db R-annotate R-AnnotationDbi R-survival R-Biobase 

BuildRequires:    R-devel tex(latex) R-Biobase R-annotate R-methods
BuildRequires:    R-SparseM R-GO.db R-annotate R-AnnotationDbi R-survival R-Biobase 


%description
SAFE is a resampling-based method for testing functional categories in
gene expression experiments. SAFE can be applied to 2-sample and
multi-class comparisons, or simple linear regressions. Other experimental
designs can also be accommodated through user-defined functions.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.14.0-1
- initial package for Fedora