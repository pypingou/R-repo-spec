%global packname  ChIPseqR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.0
Release:          1%{?dist}
Summary:          Identifying Protein Binding Sites in High-Throughput Sequencing Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-ShortRead R-methods 

BuildRequires:    R-devel tex(latex) R-ShortRead R-methods 

%description
ChIPseqR identifies protein binding sites from ChIP-seq and nucleosome
positioning experiments. The model used to describe binding events was
developed to locate nucleosomes but should flexible enough to handle other
types of experiments as well.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.0-1
- initial package for Fedora