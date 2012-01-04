%global packname  rlecuyer
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          R interface to RNG with multiple streams

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Provides an interface to the C implementation of the random number
generator with multiple independent streams developed by L'Ecuyer et al
(2002). The main purpose of this package is to enable the use of this
random number generator in parallel R applications.

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
%doc %{rlibdir}/rlecuyer/html
%doc %{rlibdir}/rlecuyer/DESCRIPTION
%{rlibdir}/rlecuyer/help
%{rlibdir}/rlecuyer/INDEX
%{rlibdir}/rlecuyer/Meta
%{rlibdir}/rlecuyer/libs
%{rlibdir}/rlecuyer/R
%{rlibdir}/rlecuyer/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora