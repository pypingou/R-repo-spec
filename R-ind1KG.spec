%global packname  ind1KG
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.11
Release:          1%{?dist}
Summary:          Data from 1000 Genomes, NA19240 (female) chr6 excerpt

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Rsamtools R-TxDb.Hsapiens.UCSC.hg18.knownGene 

BuildRequires:    R-devel tex(latex) R-Rsamtools R-TxDb.Hsapiens.UCSC.hg18.knownGene 

%description
Elements of samtools/bioc workflow for dealing with personal sequence
focusing on identification and interpretation of rare variants

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.11-1
- initial package for Fedora