%global packname  maanova
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.24.0
Release:          1%{?dist}
Summary:          Tools for analyzing Micro Array experiments

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-Biobase R-graphics R-grDevices R-methods R-stats R-utils 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-Biobase R-graphics R-grDevices R-methods R-stats R-utils 


%description
Analysis of N-dye Micro Array experiment using mixed model effect.
Containing analysis of variance, permutation and bootstrap, cluster and
consensus tree.

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
%doc %{rlibdir}/maanova/DESCRIPTION
%doc %{rlibdir}/maanova/html
%doc %{rlibdir}/maanova/doc
%{rlibdir}/maanova/help
%{rlibdir}/maanova/NAMESPACE
%{rlibdir}/maanova/LICENSE.txt
%{rlibdir}/maanova/R
%{rlibdir}/maanova/data
%{rlibdir}/maanova/TODO.txt
%{rlibdir}/maanova/libs
%{rlibdir}/maanova/INDEX
%{rlibdir}/maanova/README.txt
%{rlibdir}/maanova/demo
%{rlibdir}/maanova/Meta
%{rlibdir}/maanova/STATUS.txt

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.24.0-1
- initial package for Fedora