%global packname  MSeasy
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          5.2
Release:          1%{?dist}
Summary:          Preprocessing of Gas Chromatography-Mass Spectrometry (GC-MS) data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-amap R-clValid R-cluster R-fpc 


BuildRequires:    R-devel tex(latex) R-amap R-clValid R-cluster R-fpc



%description
Package for the detection of molecules in complex mixtures of compounds.
It creates an initial data matrix from several GC-MS analyses by
collecting and assembling the information from chromatograms and mass
spectra (MS.DataCreation). It tests for the best unsupervised clustering
method to group similar mass spectra into molecules (MS.test.clust). It
runs the optimal unsupervised clustering method on the initial data
matrix, identifies the optimal number of clusters, produces different
files for facilitating the identification of molecules and returns
fingerprinting or profiling matrices (MS.clust).

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 5.2-1
- initial package for Fedora