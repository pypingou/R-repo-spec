%global packname  GOSim
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.5
Release:          1%{?dist}
Summary:          Computation of functional similarities between GO terms and gene products; GO enrichement analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-GO.db R-AnnotationDbi R-annotate R-topGO R-cluster R-flexmix R-RBGL R-graph R-Matrix R-corpcor R-org.Hs.eg.db 

BuildRequires:    R-devel tex(latex) R-GO.db R-AnnotationDbi R-annotate R-topGO R-cluster R-flexmix R-RBGL R-graph R-Matrix R-corpcor R-org.Hs.eg.db 

%description
This package implements several functions useful for computing
similarities between GO terms and gene products based on their GO
annotation. Moreover it allows for computing a GO enrichment analysis

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.5-1
- initial package for Fedora