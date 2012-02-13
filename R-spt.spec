%global packname  spt
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.11.12.7
Release:          1%{dist}
Summary:          Sierpinski Pedal Triangle

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.11-12-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
This package collects algorithms related to Sierpinski pedal triangle

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
%doc %{rlibdir}/spt/html
%doc %{rlibdir}/spt/DESCRIPTION
%doc %{rlibdir}/spt/LICENCE
%{rlibdir}/spt/help
%{rlibdir}/spt/R
%{rlibdir}/spt/INDEX
%{rlibdir}/spt/NAMESPACE
%{rlibdir}/spt/libs
%{rlibdir}/spt/Meta

%changelog
* Sat Feb 11 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.11.12.7-1
- Update to version 1.11.12.7

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora
