%global packname  WMTregions
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.1.0.2
Release:          1%{?dist}
Summary:          Exact Calculation of WMTR

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rggobi R-RGtk2 R-rgl 


BuildRequires:    R-devel tex(latex) R-rggobi R-RGtk2 R-rgl



%description
R realization of an exact algorithm for calculating the weighted-mean
trimmed regions

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.1.0.2-1
- initial package for Fedora