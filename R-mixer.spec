%global packname  mixer
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5
Release:          1%{?dist}
Summary:          Random graph clustering

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Routines for the analysis (unsupervised clustering) of networks using
MIXtures of Erdos-Renyi random graphs

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
%doc %{rlibdir}/mixer/CITATION
%doc %{rlibdir}/mixer/NEWS
%doc %{rlibdir}/mixer/DESCRIPTION
%doc %{rlibdir}/mixer/html
%{rlibdir}/mixer/NAMESPACE
%{rlibdir}/mixer/spm
%{rlibdir}/mixer/help
%{rlibdir}/mixer/data
%{rlibdir}/mixer/INDEX
%{rlibdir}/mixer/Meta
%{rlibdir}/mixer/R
%{rlibdir}/mixer/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5-1
- initial package for Fedora