%global packname  illuminaHumanv2BeadID.db
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.8.0
Release:          1%{?dist}
Summary:          Illumina HumanWGv2 annotation data (chip illuminaHumanv2BeadID)

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-AnnotationDbi R-org.Hs.eg.db 
Requires:         R-methods R-AnnotationDbi 

BuildRequires:    R-devel tex(latex) R-methods R-AnnotationDbi R-org.Hs.eg.db
BuildRequires:    R-methods R-AnnotationDbi 


%description
Illumina HumanWGv2 annotation data (chip illuminaHumanv2BeadID) assembled
using data from public repositories to be used with data summarized from
bead-level data with numeric ArrayAddressIDs as keys. Illumina probes with
a No match or Bad quality score were removed prior to annotation. See
http://www.compbio.group.cam.ac.uk/Resources/Annotation/index.html and
Barbosa-Morais et al (2010)  A re-annotation pipeline for Illumina
BeadArrays: improving the interpretation of gene expression data. Nucleic
Acids Research.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.0-1
- initial package for Fedora