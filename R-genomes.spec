%global packname  genomes
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Genome sequencing project metadata

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice 
Requires:         R-XML 

BuildRequires:    R-devel tex(latex) R-lattice
BuildRequires:    R-XML 


%description
Collects genome sequencing project metadata from NCBI
(http://www.ncbi.nlm.nih.gov) or ENA (http://www.ebi.ac.uk/ena).

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
%doc %{rlibdir}/genomes/DESCRIPTION
%doc %{rlibdir}/genomes/doc
%doc %{rlibdir}/genomes/html
%{rlibdir}/genomes/NAMESPACE
%{rlibdir}/genomes/Meta
%{rlibdir}/genomes/ChangeLog
%{rlibdir}/genomes/R
%{rlibdir}/genomes/help
%{rlibdir}/genomes/INDEX
%{rlibdir}/genomes/data

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.0-1
- initial package for Fedora