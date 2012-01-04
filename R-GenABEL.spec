%global packname  GenABEL
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.9
Release:          1%{?dist}
Summary:          genome-wide SNP association analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.6-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-MASS 

BuildRequires:    R-devel tex(latex) R-methods R-MASS 

%description
a package for genome-wide association analysis between quantitative or
binary traits and single-nucleotide polymorphisms (SNPs).

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
%doc %{rlibdir}/GenABEL/DESCRIPTION
%doc %{rlibdir}/GenABEL/doc
%doc %{rlibdir}/GenABEL/html
%{rlibdir}/GenABEL/libs
%{rlibdir}/GenABEL/help
%{rlibdir}/GenABEL/Meta
%{rlibdir}/GenABEL/data
%{rlibdir}/GenABEL/INDEX
%{rlibdir}/GenABEL/R
%{rlibdir}/GenABEL/demo
%{rlibdir}/GenABEL/exdata
%{rlibdir}/GenABEL/unitTests
%{rlibdir}/GenABEL/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.9-1
- initial package for Fedora