%global packname  NCIgraphData
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.99.3
Release:          1%{?dist}
Summary:          Data for the NCIgraph software package

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Provides pathways from the NCI Pathways Database as R graph objects

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
%doc %{rlibdir}/NCIgraphData/DESCRIPTION
%doc %{rlibdir}/NCIgraphData/html
%{rlibdir}/NCIgraphData/INDEX
%{rlibdir}/NCIgraphData/NAMESPACE
%{rlibdir}/NCIgraphData/help
%{rlibdir}/NCIgraphData/data
%{rlibdir}/NCIgraphData/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.3-1
- initial package for Fedora