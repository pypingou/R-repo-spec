%global packname  tnet
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.0.5
Release:          1%{?dist}
Summary:          tnet: Software for Analysis of Weighted, Two-mode, and Longitudinal networks

Group:            Applications/Engineering 
License:          CC BY-NC 3.0 + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-igraph R-survival 

BuildRequires:    R-devel tex(latex) R-igraph R-survival 

%description
R package to analyse weighted, two-mode, and longitudinal networks.

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
%doc %{rlibdir}/tnet/CITATION
%doc %{rlibdir}/tnet/html
%doc %{rlibdir}/tnet/DESCRIPTION
%{rlibdir}/tnet/R
%{rlibdir}/tnet/data
%{rlibdir}/tnet/INDEX
%{rlibdir}/tnet/Meta
%{rlibdir}/tnet/help
%{rlibdir}/tnet/LICENSE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.0.5-1
- initial package for Fedora