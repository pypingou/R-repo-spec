%global packname  mosaicsExample
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.99.5
Release:          1%{?dist}
Summary:          Example data for the mosaics package, which implements MOSAiCS, a statistical framework to analyze one-sample or two-sample ChIP-seq data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Data for the mosaics package, consisting of chromosome 21 ChIP and control
sample data from a ChIP-seq experiment of STAT1 binding, with mappability,
GC content, and sequence ambiguity scores of human genome HG18.

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
%doc %{rlibdir}/mosaicsExample/DESCRIPTION
%doc %{rlibdir}/mosaicsExample/html
%{rlibdir}/mosaicsExample/help
%{rlibdir}/mosaicsExample/NAMESPACE
%{rlibdir}/mosaicsExample/extdata
%{rlibdir}/mosaicsExample/data
%{rlibdir}/mosaicsExample/INDEX
%{rlibdir}/mosaicsExample/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.5-1
- initial package for Fedora