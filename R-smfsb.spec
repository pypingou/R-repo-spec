%global packname  smfsb
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          SMfSB 2e: Stochastic Modelling for Systems Biology, second edition

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package contains code and data for modelling and simulation of
stochastic kinetic biochemical network models. It contains the code and
data associated with the second edition of the book Stochastic Modelling
for Systems Biology, published by Chapman & Hall/CRC Press, November 2011.

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
%doc %{rlibdir}/smfsb/doc
%doc %{rlibdir}/smfsb/DESCRIPTION
%doc %{rlibdir}/smfsb/html
%{rlibdir}/smfsb/INDEX
%{rlibdir}/smfsb/help
%{rlibdir}/smfsb/demo
%{rlibdir}/smfsb/NAMESPACE
%{rlibdir}/smfsb/R
%{rlibdir}/smfsb/Meta
%{rlibdir}/smfsb/libs
%{rlibdir}/smfsb/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora