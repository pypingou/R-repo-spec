%global packname  ppiPre
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Predict protein-protein interactions based on functional and topological similarities.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-AnnotationDbi R-GO.db R-KEGG.db R-org.Sc.sgd.db R-igraph R-e1071 R-org.Hs.eg.db 


BuildRequires:    R-devel tex(latex) R-AnnotationDbi R-GO.db R-KEGG.db R-org.Sc.sgd.db R-igraph R-e1071 R-org.Hs.eg.db



%description
This package implements several functions useful for computing
similarities between proteins based on their GO annotation, KEGG
annotation and PPI network topology. It integrates these similarities to
predict PPIs using an SVM classifier. Nineteen species are supported,
including Anopheles, Arabidopsis, Bovine, Canine, Chicken, Chimp, E coli
strain K12 and strain Sakai, Fly, Human, Malaria, Mouse, Pig, Rhesus, Rat,
Worm, Xenopus, Yeast, and Zebrafish.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora