%global packname  lumiBarnes
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.7
Release:          1%{?dist}
Summary:          Barnes Benchmark Illumina Tissues Titration Data

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Biobase R-lumi 

BuildRequires:    R-devel tex(latex) R-Biobase R-lumi 

%description
The Barnes benchmark dataset can be used  to evaluate the algorithms for
Illumina microarrays. It measured a titration series of two human tissues,
blood and placenta, and includes six samples with the titration ratio of
blood and placenta as 100:0, 95:5, 75:25, 50:50, 25:75 and 0:100. The
samples were hybridized on HumanRef-8 BeadChip (Illumina, Inc) in
duplicate. The data is loaded as an LumiBatch Object (see documents in the
lumi package).

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.7-1
- initial package for Fedora