%global packname  ConsensusClusterPlus
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          ConsensusClusterPlus

Group:            Applications/Engineering 
License:          GPL version 2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-Biobase R-ALL R-graphics R-stats R-utils 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-Biobase R-ALL R-graphics R-stats R-utils 


%description
algorithm for determining cluster count and membership by stability
evidence in unsupervised analysis

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
%doc %{rlibdir}/ConsensusClusterPlus/html
%doc %{rlibdir}/ConsensusClusterPlus/DESCRIPTION
%doc %{rlibdir}/ConsensusClusterPlus/doc
%{rlibdir}/ConsensusClusterPlus/Meta
%{rlibdir}/ConsensusClusterPlus/R
%{rlibdir}/ConsensusClusterPlus/NAMESPACE
%{rlibdir}/ConsensusClusterPlus/help
%{rlibdir}/ConsensusClusterPlus/INDEX

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora