%global packname  mbmdr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.4
Release:          1%{?dist}
Summary:          Model Based Multifactor Dimensionality Reduction

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-logistf 

BuildRequires:    R-devel tex(latex) R-logistf 

%description
Model Based Multifactor Dimension Reduction proposed by Calle et al.
(2008) as a dimension reduction method for exploring gene-gene

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
%doc %{rlibdir}/mbmdr/DESCRIPTION
%doc %{rlibdir}/mbmdr/html
%{rlibdir}/mbmdr/Meta
%{rlibdir}/mbmdr/R
%{rlibdir}/mbmdr/INDEX
%{rlibdir}/mbmdr/data
%{rlibdir}/mbmdr/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4-1
- initial package for Fedora