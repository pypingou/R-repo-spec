%global packname  plumbr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.5
Release:          1%{?dist}
Summary:          Mutable and dynamic data models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-utils R-methods R-objectSignals 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-utils R-methods R-objectSignals 


%description
The base R data.frame, like any vector, is copied upon modification. This
behavior is at odds with that of GUIs and interactive graphics. To rectify
this, plumbr provides a mutable, dynamic tabular data model. Models may be
chained together to form the complex plumbing necessary for sophisticated
graphical interfaces. Also included is a general framework for linking
datasets; an typical use case would be a linked brush.

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
%doc %{rlibdir}/plumbr/html
%doc %{rlibdir}/plumbr/DESCRIPTION
%{rlibdir}/plumbr/NAMESPACE
%{rlibdir}/plumbr/Meta
%{rlibdir}/plumbr/R
%{rlibdir}/plumbr/tests
%{rlibdir}/plumbr/INDEX
%{rlibdir}/plumbr/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.5-1
- initial package for Fedora