%global packname  Interpol
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Interpolation of amino acid sequences

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A package for numerical encoding as well as for linear and non-linear
interpolation of amino acid sequences.

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
%doc %{rlibdir}/Interpol/DESCRIPTION
%doc %{rlibdir}/Interpol/html
%{rlibdir}/Interpol/Meta
%{rlibdir}/Interpol/data
%{rlibdir}/Interpol/R
%{rlibdir}/Interpol/INDEX
%{rlibdir}/Interpol/NAMESPACE
%{rlibdir}/Interpol/help

%changelog
* Sat Dec 03 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.1-1
- initial package for Fedora