%global packname  spgrass6
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.4
Release:          1%{?dist}
Summary:          Interface between GRASS 6+ geographical information system and R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-sp R-rgdal R-XML 


BuildRequires:    R-devel tex(latex) R-sp R-rgdal R-XML



%description
Interpreted interface between GRASS 6+ geographical information system and
R, based on starting R from within the GRASS environment, or running
free-standing R in a temporary GRASS location; the package provides
facilities for using all GRASS commands from the R command line.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.4-1
- initial package for Fedora