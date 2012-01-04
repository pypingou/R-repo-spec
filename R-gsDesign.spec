%global packname  gsDesign
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.4.01
Release:          1%{?dist}
Summary:          Group Sequential Design

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.4-01.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-ggplot2 R-xtable 

BuildRequires:    R-devel tex(latex) R-ggplot2 R-xtable 

%description
gsDesign is a package that derives group sequential designs and describes
their properties.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4.01-1
- initial package for Fedora