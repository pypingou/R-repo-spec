%global packname  segmentSeq
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Methods for identifying small RNA loci from high-throughput sequencing data

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-baySeq R-ShortRead 

BuildRequires:    R-devel tex(latex) R-methods R-baySeq R-ShortRead 

%description
High-throughput sequencing technologies allow the production of large
volumes of short sequences, which can be aligned to the genome to create a
set of matches to the genome. By looking for regions of the genome which
to which there are high densities of matches, we can infer a segmentation
of the genome into regions of biological significance. The methods in this
package allow the simultaneous segmentation of data from multiple samples,
taking into account replicate data, in order to create a consensus
segmentation. This has obvious applications in a number of classes of
sequencing experiments, particularly in the discovery of small RNA loci
and novel mRNA transcriptome discovery.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora