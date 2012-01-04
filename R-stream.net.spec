%global packname  stream.net
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Building and analyzing binary stream networks

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Functions with example data for creating, importing, attributing,
analyzing, and displaying stream networks represented as binary trees. 
Capabilities include upstream and downstream distance matrices, stochastic
network generation, segmentation of network into reaches, adding
attributes to reaches with specified statistical distributions,
interpolating reach attributes from sparse data, analyzing autocorrelation
of reach attributes, and creating maps with legends of attribute data. 
Target applications include dynamic fish modeling.

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
%doc %{rlibdir}/stream.net/DESCRIPTION
%doc %{rlibdir}/stream.net/html
%{rlibdir}/stream.net/R
%{rlibdir}/stream.net/INDEX
%{rlibdir}/stream.net/NAMESPACE
%{rlibdir}/stream.net/help
%{rlibdir}/stream.net/README
%{rlibdir}/stream.net/Meta
%{rlibdir}/stream.net/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.6-1
- initial package for Fedora