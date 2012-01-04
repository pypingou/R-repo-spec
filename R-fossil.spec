%global packname  fossil
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.5
Release:          1%{?dist}
Summary:          Palaeoecological and Palaeogeographical Analysis Tools

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-sp R-maps 

BuildRequires:    R-devel tex(latex) R-sp R-maps 

%description
A set of analytical tools useful in analysing ecological and geographical
data sets, both ancient and modern. The package includes functions for
estimating species richness (Chao 1 and 2, ACE, ICE, Jacknife), shared
species/beta diversity, species area curves and geographic distances and

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
%doc %{rlibdir}/fossil/DESCRIPTION
%doc %{rlibdir}/fossil/html
%doc %{rlibdir}/fossil/CITATION
%{rlibdir}/fossil/help
%{rlibdir}/fossil/data
%{rlibdir}/fossil/R
%{rlibdir}/fossil/INDEX
%{rlibdir}/fossil/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.5-1
- initial package for Fedora