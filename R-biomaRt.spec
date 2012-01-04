%global packname  biomaRt
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.10.0
Release:          1%{?dist}
Summary:          Interface to BioMart databases (e.g. Ensembl, COSMIC ,Wormbase and Gramene)

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 
Requires:         R-XML R-RCurl 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-XML R-RCurl 


%description
In recent years a wealth of biological data has become available in public
data repositories. Easy access to these valuable data resources and firm
integration with data analysis is needed for comprehensive bioinformatics
data analysis.  biomaRt provides an interface to a growing collection of
databases implementing the BioMart software suite
(http://www.biomart.org). The package enables retrieval of large amounts
of data in a uniform way without the need to know the underlying database
schemas or write complex SQL queries. Examples of BioMart databases are
Ensembl, COSMIC, Uniprot, HGNC, Gramene, Wormbase and dbSNP mapped to
Ensembl. These major databases give biomaRt users direct access to a
diverse set of data and enable a wide range of powerful online queries
from gene annotation to database mining.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.10.0-1
- initial package for Fedora