%global packname  multiscan
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.14.0
Release:          1%{?dist}
Summary:          R package for combining multiple scans

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-Biobase R-utils 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-Biobase R-utils 


%description
Estimates gene expressions from several laser scans of the same microarray

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
%doc %{rlibdir}/multiscan/doc
%doc %{rlibdir}/multiscan/html
%doc %{rlibdir}/multiscan/DESCRIPTION
%{rlibdir}/multiscan/Meta
%{rlibdir}/multiscan/libs
%{rlibdir}/multiscan/help
%{rlibdir}/multiscan/R
%{rlibdir}/multiscan/INDEX
%{rlibdir}/multiscan/data
%{rlibdir}/multiscan/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.14.0-1
- initial package for Fedora