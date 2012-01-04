%global packname  Rwave
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.25.1
Release:          1%{?dist}
Summary:          Time-Frequency analysis of 1-D signals

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.25-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Rwave is a library of R functions which provide an environment for the
Time-Frequency analysis of 1-D signals (and especially for the wavelet and
Gabor transforms of noisy signals). It was originally written for Splus by
Rene Carmona, Bruno Torresani, and Wen L. Hwang, first at the University
of California at Irvine and then at Princeton University.  Credit should
also be given to Andrea Wang whose functions on the dyadic wavelet
transform are included. Rwave is based on the book: "Practical
Time-Frequency Analysis: Gabor and Wavelet Transforms with an
Implementation in S", by Rene Carmona, Wen L. Hwang and Bruno Torresani,
Academic Press, 1998.

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
%doc %{rlibdir}/Rwave/html
%doc %{rlibdir}/Rwave/NEWS
%doc %{rlibdir}/Rwave/DESCRIPTION
%{rlibdir}/Rwave/INDEX
%{rlibdir}/Rwave/help
%{rlibdir}/Rwave/demo
%{rlibdir}/Rwave/NAMESPACE
%{rlibdir}/Rwave/R
%{rlibdir}/Rwave/Meta
%{rlibdir}/Rwave/libs
%{rlibdir}/Rwave/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.25.1-1
- initial package for Fedora