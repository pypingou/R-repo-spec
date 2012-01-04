%global packname  OligoSpecificitySystem
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Oligo Specificity System

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk R-tkrplot 

BuildRequires:    R-devel tex(latex) R-tcltk R-tkrplot 

%description
Calculate the theorical specificity of a system of multiple primers used
for PCR, qPCR primers or degenerated primer design

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
%doc %{rlibdir}/OligoSpecificitySystem/html
%doc %{rlibdir}/OligoSpecificitySystem/DESCRIPTION
%doc %{rlibdir}/OligoSpecificitySystem/doc
%{rlibdir}/OligoSpecificitySystem/NAMESPACE
%{rlibdir}/OligoSpecificitySystem/help
%{rlibdir}/OligoSpecificitySystem/R
%{rlibdir}/OligoSpecificitySystem/INDEX
%{rlibdir}/OligoSpecificitySystem/tcltk.gif
%{rlibdir}/OligoSpecificitySystem/Rlogo.gif
%{rlibdir}/OligoSpecificitySystem/Thumbs.db
%{rlibdir}/OligoSpecificitySystem/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora