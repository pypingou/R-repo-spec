%global packname  NuPoP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          An R package for nucleosome positioning prediction

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
NuPoP is an R package for Nucleosome Positioning Prediction.This package
is built upon a duration hidden Markov model proposed in Xi et al, 2010;
Wang et al, 2008. The core of the package was written in Fotran. In
addition to the R package, a stand-alone Fortran software tool is also
available at http://nucleosome.stats.northwestern.edu.

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
%doc %{rlibdir}/NuPoP/DESCRIPTION
%doc %{rlibdir}/NuPoP/doc
%doc %{rlibdir}/NuPoP/html
%{rlibdir}/NuPoP/R
%{rlibdir}/NuPoP/NAMESPACE
%{rlibdir}/NuPoP/extdata
%{rlibdir}/NuPoP/INDEX
%{rlibdir}/NuPoP/libs
%{rlibdir}/NuPoP/help
%{rlibdir}/NuPoP/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora