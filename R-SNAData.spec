%global packname  SNAData
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.3
Release:          1%{?dist}
Summary:          Social Networks Analysis Data Examples

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graph 

BuildRequires:    R-devel tex(latex) R-graph 

%description
Data from Wasserman & Faust (1999) "Social Network Analysis"

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
%doc %{rlibdir}/SNAData/DESCRIPTION
%doc %{rlibdir}/SNAData/doc
%doc %{rlibdir}/SNAData/html
%{rlibdir}/SNAData/NAMESPACE
%{rlibdir}/SNAData/Meta
%{rlibdir}/SNAData/INDEX
%{rlibdir}/SNAData/R
%{rlibdir}/SNAData/data
%{rlibdir}/SNAData/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.3-1
- initial package for Fedora