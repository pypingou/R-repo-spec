%global packname  dtt
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Discrete Trigonometric Transforms

Group:            Applications/Engineering 
License:          GPL version 2 or newer. http://www.gnu.org/copyleft/gpl.html
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package provides functions for 1D and 2D Discrete Cosine Transform
(DCT), Discrete Sine Transform (DST) and Discrete Hartley Transform (DHT).

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
%doc %{rlibdir}/dtt/DESCRIPTION
%doc %{rlibdir}/dtt/html
%{rlibdir}/dtt/INDEX
%{rlibdir}/dtt/help
%{rlibdir}/dtt/R
%{rlibdir}/dtt/NAMESPACE
%{rlibdir}/dtt/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora