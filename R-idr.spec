%global packname  idr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Irreproducible discovery rate

Group:            Applications/Engineering 
License:          LGPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This is a package for estimating the copula mixture model and plotting
correspondence curves in "Measuring reproducibility of high-throughput
experiments" (2011), Annals of Applied Statistics, by Li, Brown, Huang,
and Bickel

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
%doc %{rlibdir}/idr/html
%doc %{rlibdir}/idr/DESCRIPTION
%{rlibdir}/idr/help
%{rlibdir}/idr/R
%{rlibdir}/idr/INDEX
%{rlibdir}/idr/NAMESPACE
%{rlibdir}/idr/data
%{rlibdir}/idr/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora