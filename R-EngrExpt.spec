%global packname  EngrExpt
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.8
Release:          1%{?dist}
Summary:          Data sets from "Introductory Statistics for Engineering Experimentation"

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-lattice 

%description
Datasets from Nelson, Coffin and Copeland "Introductory Statistics for
Engineering Experimentation" (Elsevier, 2003) with sample code.

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
%doc %{rlibdir}/EngrExpt/html
%doc %{rlibdir}/EngrExpt/DESCRIPTION
%{rlibdir}/EngrExpt/INDEX
%{rlibdir}/EngrExpt/NAMESPACE
%{rlibdir}/EngrExpt/TXT.zip
%{rlibdir}/EngrExpt/dataplots.Rout
%{rlibdir}/EngrExpt/dataplots.R
%{rlibdir}/EngrExpt/dataplots.pdf
%{rlibdir}/EngrExpt/data
%{rlibdir}/EngrExpt/extract.R
%{rlibdir}/EngrExpt/Meta
%{rlibdir}/EngrExpt/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.8-1
- initial package for Fedora