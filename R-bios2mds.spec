%global packname  bios2mds
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          From BIOlogical Sequences to MultiDimensional Scaling

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-gtools R-amap R-e1071 R-ggplot2 R-cluster R-rgl 

BuildRequires:    R-devel tex(latex) R-gtools R-amap R-e1071 R-ggplot2 R-cluster R-rgl 

%description
Bios2mds is primarily dedicated to the analysis of biological sequences by
metric MultiDimensional Scaling with projection of supplementary data. It
contains functions for reading multiple sequence alignment files,
calculating distance matrices, performing metric multidimensional scaling
and visualizing results.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora